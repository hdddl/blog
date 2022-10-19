import re

DELIMITER = u"==========\r\n"


def get_book_index(book_name, all_books):
    """get book's index"""
    for i in range(len(all_books)):
        if all_books[i]["name"] == book_name:
            return i
    return -1


def render(content):
    all_books = []
    all_marks = []

    content = content.replace("\r\n\r\n", "\n")
    all_marks = content.split(DELIMITER)
    for i in range(len(all_marks)):
        mark = all_marks[i].split("\n")
        if len(mark) == 4:
            book_info = re.split(r"[()<>|\[\]（）《》【】｜]\s*", mark[0])
            book_name = book_info[0] if str(book_info[0]) != "" else (mark[0])
            book_author = book_info[-2] if len(book_info) > 1 else ""
            mark_info = mark[1].split("|")
            mark_time = mark_info[1]
            mark_address = mark_info[0].strip("- ")
            mark_content = mark[2]

            book_index = get_book_index(book_name, all_books)
            if book_index == -1:
                all_books.append(
                    {
                        "name": book_name,
                        "author": book_author,
                        "nums": 0,
                        "marks": [],
                    }
                )
            all_books[book_index]["marks"].append(
                {"time": mark_time, "address": mark_address, "content": mark_content}
            )
            all_books[book_index]["nums"] += 1
    all_books.sort(key=lambda x: x["nums"], reverse=True)
    return all_books
