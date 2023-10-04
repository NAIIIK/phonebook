from view import *
from database import *

def main():
    while True:
        res = select_op()
        match res:
            case 1:
                add_info(get_info())
            case 2:
                delete_info(search())
            case 3:
                change_info(search())
            case 4:
                search_info(search())
            case 5:
                print(book_view())
            case 6:
                break


main()