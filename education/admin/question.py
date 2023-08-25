from django.contrib import admin
from django.utils.translation import gettext_lazy as _
from django import forms
from grappelli.forms import GrappelliSortableHiddenMixin

from education.models import Question, Answer


class AnswerForm(GrappelliSortableHiddenMixin, forms.ModelForm):
    class Meta:
        model = Answer
        fields = '__all__'


class AnswerFormset(forms.BaseInlineFormSet):
    def clean(self):
        super(AnswerFormset, self).clean()
        # Check that only one answer is correct
        if any(self.errors):
            return
        answer_type = self.instance.type_answer
        if answer_type == 'unique_choice':
            correct_answers = 0
            for form in self.forms:
                if form.cleaned_data and form.cleaned_data.get('is_correct'):
                    correct_answers += 1
            if correct_answers != 1:
                raise forms.ValidationError(_('Only one answer can be correct.'))
        elif answer_type == 'multiple_choice':
            correct_answers = 0
            for form in self.forms:
                if form.cleaned_data and form.cleaned_data.get('is_correct'):
                    correct_answers += 1
            if correct_answers < 1:
                raise forms.ValidationError(_('At least one answer must be correct.'))
        else:
            ans = []
            for form in self.forms:
                if form.cleaned_data and form.cleaned_data.get('match'):
                    ans.append(form.cleaned_data.get('match'))

            # Check that all answers are even
            ans.sort()
            if len(ans) % 2 != 0:
                raise forms.ValidationError(_('All answers must be even.'))
            
            # Check that all answers are twice
            for i in range(0, len(ans), 2):
                if ans[i] != ans[i+1]:
                    raise forms.ValidationError(_('All answers must be twice.'))
            # Check that all answers are used
            if ans[0] == 0:
                raise forms.ValidationError(_('All answers must be used.'))
            
            # Check that all couples are unique
            if len(ans) != len(set(ans)) * 2:
                raise forms.ValidationError(_('All couples must be unique.'))



class QuestionAnswerInline(admin.TabularInline):
    model = Answer
    extra = 4
    formset = AnswerFormset
    # form = AnswerForm

    def get_extra(self, request, obj=None, **kwargs):
        if obj:
            return 0
        return self.extra


class QuestionAdmin(admin.ModelAdmin):
    autocomplete_fields = (
        'author',
        'category',
        'level'
    )

    inlines = [
        QuestionAnswerInline,
    ]

    list_display = (
        'code',
        'level',
        'category',
        'author',
    )