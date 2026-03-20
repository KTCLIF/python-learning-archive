'''
    위의 posts에 담긴 데이터를 이용해서 아래와 같이 출력되도록 해보세요.

    글목록 입니다.
    - 글번호: 1  작성자: 작성자 1  제목: 제목1
    - 글번호: 2  작성자: 작성자 2  제목: 제목2
    - 글번호: 3  작성자: 작성자 3  제목: 제목3
'''

from jinja2 import Template

#게시글 목록이 담긴 리스트
posts: list = [
    {"id": 1, "writer": "작성자1", "title": "제목1"},
    {"id": 2, "writer": "작성자2", "title": "제목2"},
    {"id": 3, "writer": "작성자3", "title": "제목3"}
]

if __name__ == "__main__":
    temp_str = """
    글목록 입니다.
    {% for p in posts_list %}
    - 글번호: {{ p.id }}  작성자: {{ p.writer }}  제목: {{ p.title }}
    {% endfor %}
    """
    
    tm = Template(temp_str)
    
    result = tm.render(posts_list=posts)
    
    print(result)

# ///////아래는 정답

posts_template = '''
    글목록 입니다.
    {% for post in posts %}
    - 글번호: {{ post.id }}  작성자: {{ post.writer }}  제목: {{ post.title }}
    {% endfor %}
'''


#Template 객체를 생성하고
temp:Template = Template(posts_template)


# Template 객체의 render() 메소드를 이용해서 결과를 얻어낸다.
result:str = temp.render(posts=posts)
print(result)

