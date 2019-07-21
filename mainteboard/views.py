from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import Regist
from .forms import NewRegistForm
#一覧
def index(request):
    regists = Regist.objects.all()
    return render(request, 'mainteboard/index.html', {'regists': regists})

#新規と編集
def create(request):
    #form登録用のビュー
    form = NewRegistForm()
    #formインスタンスの作成
    if request.method == 'POST':
    #画面からPOSTした場合、実行
        form = NewRegistForm(request.POST)
            #画面からPOSTした値を取得
        if form.is_valid():
            form.save(commit=True)
                #form.saveするとデータが登録される
            return index(request)
        else:
            print("ERROR FORM INVALID")
    return render(request, 'mainteboard/create.html', {'form': form})
        #POSTしない場合の画面にformを渡す


def read(request, id):
    regist = Regist.objects.get(id=id)
    #regist = get_object_or_404(Regist, id=id)
    return render(request, 'mainteboard/read.html', {'regist': regist})

def update(request, id):
    regist = get_object_or_404(Regist, id=id)
    if request.method == "POST":
        form = NewRegistForm(request.POST, instance=regist)
        if form.is_valid():
            form.save(commit=True)
            #return index(request)
            return render(request, 'mainteboard/read.html', {'regist': regist})
        else:
            print("ERROR FORM INVALID")
    else:
        form = NewRegistForm(instance=regist)
    return render(request, 'mainteboard/update.html', {'form': form})




#詳細（おまけ）
def delete(request, id=None):
    return HttpResponse("削除")
