class upload:
    def __init__(self):
        self.name = ''
        self.category = ''
        self.price = 0
        self.explanation = ''
        self.furniture = set() #가구
        self.appliances = set() #가전제품
        self.clothing = set() #의류
        self.accessoria = set() #악세사리
        self.product_list = {}

    def set_product(self):
        self.set_name()
        self.set_category()
        self.set_price()
        self.set_explanation()
        self.product_list[self.name] = self.price

    def set_name(self):
        self.name = input('업로드 할 제품을 입력하세요. :')

        def set_category(self):  
            print(f'1.가구 2. 가전제품 3. 의류 4. 악세사리')
            self.category = input("상품의 카테고리를 선택하세요. :")
        
        if self.category == '1':
            self.furniture.add(self.name)
            category_name = '가구'
        elif self.category == '2':
            self.appliances.add(self.name)
        elif self.category == '3':
            self.clothing.add(self.name)
        elif self.category == '4':
            self.accessoria.add(self.name)
        else:
            print("잘못 입력하셨습니다.")

    def set_price(self):
        self.price = input("가격을 입력하세요. :")
        self.price = int(self.price)
        if self.price <= 0  and self.price > 50000 :
            print("금액은 0부터 50,000원까지 입력 가능합니다.")
            self.set_product()
            #다시 입력받는 


    def set_explantion(self):
        self.explanation = input("제품에 대한 설명을 작성하세요. :")
        print(f'\n{self.name}\n 카테고리 : {self.category_name}\t 가격 : {self.price}\t 제품설명 : {self.explanation}\n\n')

    def __str__(self):
        return f'{self.name}\n 카테고리 : {self.category}\t 가격 : {self.price}\t 제품설명 : {self.explanation}' #대괄호 안에 f 쓰면 연결
