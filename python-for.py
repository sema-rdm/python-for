#!/usr/bin/env python
# coding: utf-8

# In[2]:


for i in range(11):
    print(i)


# In[2]:


meyveler=["armut", "elma","karpuz","kiraz","limon"]
for x in meyveler:
    print(x)


# In[3]:


len(meyveler)


# In[4]:


meyveler[len(meyveler)-1]


# In[3]:


for a in "AYŞE":
    print(a)


# In[7]:


for x in meyveler:
    print(x)
    if x=="kiraz":
        break


# In[11]:


for i in range(0,11):
    if(i==6 or i==7):
        continue
    print(i)


# In[13]:


for i in range(1,4):
    print("ilk döngü sayısı: %d" %i)
    for j in range(1,5):
        print("ikinci döngü sayısı : %d" %j)


# In[4]:


kullanici_adi="ebyu"
kullanici_sifre="1234"
sayac=4
for i in range(1,4):
    print("doğru giriş için kalan hakkınız: %d\n" %(sayac-1))
    kul_adi=input("kullanıcı adını giriniz:")
    sifre=input("şifreyi giriniz:")
    if(kul_adi==kullanici_adi and sifre==kullanici_sifre):
        print("sisteme giriş yapıldı")
        break
    elif(kul_adi!=kullanici_adi and sifre!=kullanici_sifre):
        print("kullanıcı adı veya şifre hatalı\n")
    else:
        print("yanlış değer girdiniz")
        sayac-=1
    if(sayac==1):
        print("giriş yasaklandı")


# In[ ]:





# In[ ]:




