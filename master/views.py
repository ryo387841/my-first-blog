from django.shortcuts import render, redirect
from django.http import HttpResponse
# Create your views here.


from .models import User,Division,Content
from .forms import NewUserForm,NewDivisionForm,NewContentForm

from django.views.decorators.http import require_POST

#一覧
def index(request):
    lists = [{'master_name':'ユーザー','path':'user'},{'master_name':'区分','path':'division'},{'master_name':'内容','path':'content'}]
    return render(request, 'master/index.html', {'lists': lists})

def user_index(request):
    users = User.objects.all()
    return render(request, 'master/user_index.html', {'users': users})

def user_create(request):
    #form登録用のビュー
    form = NewUserForm()
    #formインスタンスの作成
    if request.method == 'POST':
    #画面からPOSTした場合、実行
        form = NewUserForm(request.POST)
            #画面からPOSTした値を取得
        if form.is_valid():
            form.save(commit=True)
                #form.saveするとデータが登録される
            return user_index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'master/user_create.html', {'form': form})
        #POSTしない場合の画面にformを渡す

#-------------------------------------------------------------------------
#ここからDivision
def division_index(request):
    divisions = Division.objects.all()
    return render(request, 'master/division_index.html', {'divisions': divisions})

def division_create(request):
    #form登録用のビュー
    form = NewDivisionForm()
    #formインスタンスの作成
    if request.method == 'POST':
    #画面からPOSTした場合、実行
        form = NewDivisionForm(request.POST)
            #画面からPOSTした値を取得
        if form.is_valid():
            form.save(commit=True)
                #form.saveするとデータが登録される
            return division_index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'master/division_create.html', {'form': form})
        #POSTしない場合の画面にformを渡す

#-------------------------------------------------------------------------
#ここからContent
def content_index(request):
    contents = Content.objects.all()
    return render(request, 'master/content_index.html', {'contents': contents})

def content_create(request):
    #form登録用のビュー
    form = NewContentForm()
    #formインスタンスの作成
    if request.method == 'POST':
    #画面からPOSTした場合、実行
        form = NewContentForm(request.POST)
            #画面からPOSTした値を取得
        if form.is_valid():
            form.save(commit=True)
                #form.saveするとデータが登録される
            return content_index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'master/content_create.html', {'form': form})
        #POSTしない場合の画面にformを渡す
