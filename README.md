# UIUX_G40
Ứng dụng sử dụng Flask của Python và Docker để triển khai localhost, vì vậy thiết bị cần có sẵn Python
Thực hiện các bước như sau:
1. Cài đặt các thư viện cần thiết
     pip install Flask<br />
     pip install sqlalchemy<br />
     pip install psycopg2<br />

2. Cài đặt docker từ website của Docker và thực hiện câu lệnh:<br />
   docker volume create db_uiux<br />
   docker-compose up -d<br />

3. Sau khi hoàn thành 2 bước trên, thực hiện câu lệnh python app.py

Lưu ý: tất cả các bước trên đều cần được thực hiện trên terminal với môi trường Python
        
