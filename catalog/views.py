from django.shortcuts import render
from .models import Book , Author , BookInstance , Genre
from django.views import generic
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

#view for home page
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    #'a' is available
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors =Author.objects.count()
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits+1

    context = {
        'num_books' : num_books,
        'num_instances' : num_instances,
        'num_instances_available': num_instances_available,
        'num_authors':num_authors,
        'num_visits':num_visits,
    }

    return render(request , 'index.html' , context=context)

#class for list view
class BookListView(generic.ListView):
    model = Book
    paginate_by = 1

    def get_queryset(self):
        return Book.objects.filter(title__icontains='for')[:5]

#class for detail view
class BookDetailView(generic.DetailView):
    model = Book

    def book_detail_view(requset , primary_key):
        book = get_object_or_404(Book , pk=primary_key)
        return render(requset , 'catalog/book_detail.html' , context={'book':book})


class LoanedBooksByUserListView(LoginRequiredMixin , generic.ListView):
    model = BookInstance
    template_name = 'catalog/bookinstance_list_borrowed_user.html'
    paginate_by = 10

    def get_queryset(self):
        return BookInstance.objects.filter(borrower=self.request.user).filter(status__exact='o').order_by('due_back')