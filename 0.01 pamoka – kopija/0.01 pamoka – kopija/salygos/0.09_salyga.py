# mes zinok kad validuotas pazimys yra 1<=p<=10
paz = int(input("p=..."))

def artinka():
    paz = int(input("p=..."))
    if not (1<=paz<=10):
        print('Netinkamas kartokite ivedima')
        return artinka()
    else:
        print('Pazimys tinkamas')
p = artinka()
print(paz)