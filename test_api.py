import requests
import json
import concurrent.futures

def send_request(user_question):
    url = 'http://localhost:5000/chat'
    headers = {'Content-Type': 'application/json'}
    data = {'user_question': user_question}
    response = requests.post(url, headers=headers, data=json.dumps(data))
    return response.json()

if __name__ == "__main__":
    # Danh sách các câu hỏi từ người dùng
    user_questions = [
    "Bạn có biết về trường UET",
    "Trường UET có ngành học gì",
    "Các khoa nào dẫn đầu",
    "Chương trình học 1 số ngành tiêu biểu",
    "Chương trình học Công nghệ thông tin",
    "Chương trình học Khoa học máy tính",
    "Cơ sở dữ liệu",
    "Hệ quản trị là môn gì"]
    # "Giảng viên Phan Xuân Hiếu giảng dạy gì",
    # "Trường UET nằm ở đâu",
    # "UET có ký túc xá không",
    # "Học phí của trường UET là bao nhiêu",
    # "Điều kiện tuyển sinh vào UET",
    # "UET có chương trình học bổng không",
    # "Các ngành đào tạo sau đại học ở UET",
    # "Môi trường học tập ở UET như thế nào",
    # "Cơ hội việc làm sau khi tốt nghiệp UET",
    # "Hoạt động ngoại khóa ở UET",
    # "Thời gian đào tạo của các ngành ở UET",
    # "UET có các câu lạc bộ gì",
    # "Giảng viên UET có trình độ như thế nào",
    # "Chương trình liên kết quốc tế của UET",
    # "UET có chương trình trao đổi sinh viên không"]
    # # "Thư viện của UET có những gì",
    # "UET có phòng thí nghiệm không",
    # "Cơ sở vật chất của UET"
    # "Phương pháp giảng dạy ở UET",
    # "UET có đào tạo ngành Kỹ thuật phần mềm không",
    # "Ngành Hệ thống thông tin ở UET",
    # "Công nghệ truyền thông tại UET",
    # "Khoa học dữ liệu tại UET",
    # "UET có chương trình học trực tuyến không",
    # "Cách thức đăng ký vào UET",
    # "Các môn học cơ bản tại UET",
    # "Chương trình thực tập tại UET",
    # "UET có các ngành nghiên cứu khoa học không",
    # "UET có chương trình hỗ trợ tài chính không",
    # "Các ngành kỹ thuật tại UET",
    # "Ngành Điện tử - Viễn thông tại UET",
    # "Ngành Vật lý kỹ thuật tại UET",
    # "UET có đào tạo ngành Kỹ thuật y sinh không",
    # "Giảng viên nổi tiếng của UET",
    # "UET có cơ hội nghiên cứu không",
    # "Chương trình đào tạo tiến sĩ tại UET",
    # "Cách thức nộp hồ sơ vào UET",
    # "Thời gian khai giảng tại UET",
    # "Các phòng ban hỗ trợ sinh viên tại UET",
    # "Chất lượng giảng dạy tại UET"

    user_questions1 = [
    "Curriculum of some notable majors",
    "Curriculum of Information Technology",
    "Curriculum of Computer Science",
    "What is Database",
    "What is Database Management System",
    "Do you have study materials"
    "What is Data Science",
    "Curriculum of Software Engineering",
    "What is Machine Learning",
    "What is Artificial Intelligence",
    "What is Cybersecurity",
    "Curriculum of Electrical Engineering",
    "What is Cloud Computing",
    "What is Data Mining",
    "Curriculum of Mechanical Engineering",
    "What is Network Security",
    "Do you have online courses",
    "Curriculum of Civil Engineering",
    "What is Big Data",
    "What is Blockchain"]
    # "What is Quantum Computing",
    # "Curriculum of Business Administration",
    # "What is Internet of Things",
    # "What is Virtual Reality",
    # "Curriculum of Biotechnology",
    # "What is Augmented Reality",
    # "What is Natural Language Processing",
    # "Curriculum of Chemical Engineering",
    # "What is Robotics",
    # "What is Computer Vision",
    # "Do you have programming tutorials",
    # "Curriculum of Aerospace Engineering",
    # "What is Bioinformatics",
    # "What is Ethical Hacking",
    # "What is Software Development",
    # "Curriculum of Environmental Science",
    # "What is Human-Computer Interaction",
    # "What is Embedded Systems",
    # "Curriculum of Mathematics",
    # "What is Systems Engineering",
    # "What is Business Intelligence",
    # "What is LLM",
    # "What is SLM",
    # "What is based-rule model",
    # "What is language model",
    # "What is torch",
    # "What is data understading",
    # "What is regression",
    # "What is clustering",
    # "What is data scientist"]



    # Sử dụng concurrent.futures để gửi nhiều request cùng một lúc
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Gửi các request và thu thập kết quả
        results = executor.map(send_request, user_questions)

    # In kết quả
    for result in results:
        print(result)
