

#Question 1
print("\n\nQ1.\n")

data = {'Name':['Ajitesh Nair'],'Age':[19],'mail id':['ajiteshnair10@gmail.com'],'phone no':['123345456789']}
df = pd.DataFrame(data)

df.loc[1] = ['Ritesh Singh',20,'gettoritesh@gmail.com','987654321']       
df.loc[2] = ['Mahen Gandhi',18,'imlegend19@gmail.com','567894321']

print(df)
print("\n")

#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+


#Question 2
print("\n\nQ2.\n")

df = pd.read_csv('weather.csv')

print("a). ",df.head(5))       #for first 5 
print("b). ",df.head(10))      #for first 10

print("c). ",df['MinTemp'].describe())     #list details of MinTemp keys
print(df['MaxTemp'].describe())     #Max temp key is described

print("d). ",df.tail(5))                   #last 5 are displayed

finaldata = [df.iloc[:,2].sum(),            #find basic stats
df.iloc[:,2].mean(),
df.iloc[:,2].median(),
df.iloc[:,2].nunique(),
df.iloc[:,2].max(),
df.iloc[:,2].min()]

print(finaldata) 


#=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+=+

