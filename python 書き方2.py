ライブラリ＞パッケージ＞モジュール
モジュール=関数やクラスなどをまとめて書いたファイル
パッケージ＝モジュールと__init__.pyを含むディレクトリ
名前空間パッケージ=パッケージに__init__を含まない
1.標準ライブラリ
2.サードパーティーライブラリ
3.ローカルライブラリ(自作のライブラリ）
のじゅんばんでimportする
import *はモジュール内で名前空間に__all__があるかないかでできるか決まる

パッケージからモジュールをインポート
import urllib
print(urllib.error)#AttributeError
#urllibの配下のモジュール使えない
from urllib import error
(import numpyはまるなりゆう)
numpyディレクトリの__init__でサブパッケージをインポートしているから
(scikit-learnはだめ)
ModuleNotFoundError=モジュールが存在しない
AttributeError=属性がimport下モジュールに存在しない

#レコード(テーブルの１行）取得(field属性ではカラムしか指定できない)
from django.shortcuts import get_object_or_404

class book(ListView):
    model=Book
    book=get_object_or_404(モデル,pk=book_id(レコード主キー)(第２引数以降はフィルタかけること可能,name=bookなど))
    paginate_by=5#100けんデータあったら、1ページに５件まで
    query_set=Book.objects.filter(some_column=foo)#フィルター
    form_class=AsForm
フォーム(forms.py)
class AsForm(forms.ModelForm):
    class Meta:
        model=
        fields=("name",)(カラムorリスト)
import django.views.generic.edit import CreateView
csrf form method="post" で送った時に使う



