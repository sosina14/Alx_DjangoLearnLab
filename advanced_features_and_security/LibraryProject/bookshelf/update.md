new_book = Book.objects.filter(title='1984')
book.title="Nineteen Eighty-Four"
book.save()
> The above command is used to retrive and update the new_book instances title from 1984 to Nineteen Eighty-Four.