from uploading import upload

def show_menu():
    print(f'1.상품 업로드하기 \t 2. 구매희망 \t 3. 검색기능 \t 4. 찜하기 \t 5. 종료')
    answer = input('원하는 서비스를 선택하세요: ')
    return answer

def main():
    mart = upload()
    while True:
        answer = show_menu()
        if answer == '1':
            mart.set_product() #상품추가
        elif answer == '2':
            pass
        elif answer == '3':
            pass
        elif answer == '4':
            pass 
        elif answer == '5':
            pass
        else :
            print("다시 입력하세요. ")

if __name__ == '__main__':
    main()