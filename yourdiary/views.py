import logging

from django.urls import reverse_lazy

from django.views import generic

from .forms import InquiryForm

# 画面に各種メッセージを表示するためのライブラリ
from django.contrib import messages

#ログの取得
logger = logging.getLogger(__name__)

# Create your views here.
class IndexView(generic.TemplateView):
    template_name = "index.html"

class InquiryView(generic.FormView):
    template_name = "inquiry.html"
    form_class = InquiryForm
    #処理に問題なかった場合に指定のURLにリダイレクトするための記載。
    #「reverse_lazy」関数でURLの逆引きができる。※reverse_lazy(アプリ名：ルーティングの名称)
    success_url = reverse_lazy('yourdiary:inquiry')

    #親クラスで定義されているメソッド。formの引数にformオブジェクトが格納されている。
    def form_valid(self, form):
        #メール送信制御の呼び出し
        form.send_email()
        #メッセージレベルに対応したメッセージを設定可能。
        #メッセージレベル：ERROR WARNING SUCCESS INFO
        messages.success(self.request,'送信完了じゃ')
        logger.info('Inquiry sent by {}'.format(form.cleaned_data['name']))
        return super().form_valid(form)