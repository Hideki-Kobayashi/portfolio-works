<template>
  <div class="portfolio">
    <div class="portfolio__header">
      <div class="header-catch">Portfolio</div>
    </div>
    <div class="portfolio__content port-content">

      <div class="port__table-of-contents">
        <div>目次</div>
        <a class="table-of-contents__item" href="#html/css">１、html/css</a>
        <a class="table-of-contents__item" href="#vue">２、Vue.js</a>
        <a class="table-of-contents__item" href="#python">３、Python</a>
      </div>

      <div id="html/css" class="port__item">
        <div class="item__category">html/css</div>

        <div class="item__grid">
          <div class="card">
            <a href="http://eclaircom.html.xdomain.jp/portfolio/kobayahshi-hideki/works/valu_copy/" target="_blank">
              <div class="card__title">Valuのトレース</div>
              <div class="card__img"><img src="../assets/img/valu.png" alt=""></div>
            </a>
            <div class="card__discription">Valuのサイトを、ソースを読まずに見た目をトレースしました。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/tree/master/html%26css/valu_copy" target="_blank">gitはこちら</a>
          </div>

        </div>
      </div>

      <div id="vue" class="port__item">
        <div class="item__category">Vue.js</div>

        <div class="item__grid">
          <div class="card">
            <a href="" target="_blank">
              <div class="card__title">このポートフォリオサイト</div>
              <div class="card__img"><img src="../assets/img/portfolio.png" alt=""></div>
            </a>
            <div class="card__discription">Vue.jsでSPA(シングルページアプリケーション)を実装しています。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/tree/master/Vue.js/portfolio" target="_blank">gitはこちら</a>
          </div>

          <div class="card">
            <a href="http://eclaircom.html.xdomain.jp/vue-chat/" target="_blank">
              <div class="card__title">Vueのチャットアプリ</div>
              <div class="card__img"><img src="../assets/img/vue-chat.png" alt=""></div>
            </a>
            <div class="card__discription">Twitterアカウントでログインできるシンプルなチャットアプリです。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/tree/master/Vue.js/vue-chat" target="_blank">gitはこちら</a>
          </div>

          <div class="card">
            <a href="http://praisetodo.html.xdomain.jp/" target="_blank">
              <div class="card__title">VueのTodoアプリ</div>
              <div class="card__img"><img src="../assets/img/todo.png" alt=""></div>
            </a>
            <div class="card__discription">Todoの項目と締切日を登録できるTodoアプリです。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/tree/master/Vue.js/self_quest" target="_blank">gitはこちら</a>
          </div>

          <div class="card">
            <a href="http://eclaircom.html.xdomain.jp/hello-spa/" target="_blank">
              <div class="card__title">IPを取得するSPA</div>
              <div class="card__img"><img src="../assets/img/hello-spa.png" alt=""></div>
            </a>
            <div class="card__discription">SPAで表示切替を行い、「IPを取得」ボタンを押すとIPアドレスが取得できます。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/tree/master/Vue.js/hello-spa" target="_blank">gitはこちら</a>
          </div>


        </div>
      </div>

      <div id=python class="port__item">
        <div class="item__category">Python</div>

        <div class="item__grid">
          <div class="card">
            <a href="https://pytech-todoapp.herokuapp.com/app/top" target="_blank">
              <div class="card__title">Todoアプリ</div>
              <div class="card__img"><img src="../assets/img/python-todo.png" alt=""></div>
            </a>
            <div class="card__discription">Python/Djangoでtodo機能からログイン機能まで実装しています。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/tree/master/python/pytech-todoapp" target="_blank">gitはこちら</a>
          </div>

          <div class="card">
            <a href="" target="_blank">
              <div class="card__title">人工知能チャットボット</div>
              <div class="card__img"><img src="../assets/img/python-chatbot.png" alt=""></div>
            </a>
            <div class="card__discription">シェルで会話をします。こちらの入力した文章を品詞分解し学習していきます。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/tree/master/python/unmo" target="_blank">gitはこちら</a>
          </div>

          <div class="card">
            <a href="" target="_blank">
              <div class="card__title">日経平均のスクレイピング</div>
              <div class="card__img"><img src="../assets/img/python-nikkei.png" alt=""></div>
            </a>
            <div class="card__discription">日経新聞のサイトから、日経平均株価をスクレイピングします。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/tree/master/python/%E3%82%B9%E3%82%AF%E3%83%AC%E3%82%A4%E3%83%94%E3%83%B3%E3%82%B0" target="_blank">gitはこちら</a>
          </div>
          
          <div class="card">
            <a href="" target="_blank">
              <div class="card__title">Twitterの自動いいね</div>
              <div class="card__img"><img src="../assets/img/auto-like.png" alt=""></div>
            </a>
            <div class="card__discription">特定の文字列を含むツイートを自動いいねします。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/blob/master/python/Twitter_programs/autoLike.py" target="_blank">gitはこちら</a>
          </div>
          
          <div class="card">
            <a href="" target="_blank">
              <div class="card__title">Twitterの自動リムーブ</div>
              <div class="card__img"><img src="../assets/img/auto-remove.png" alt=""></div>
            </a>
            <div class="card__discription">フォロワー100人以下のフォローを解除します。</div>
            <a class="card__link" href="https://github.com/Hideki-Kobayashi/portfolio-works/blob/master/python/Twitter_programs/autoFollowerRemove.py" target="_blank">gitはこちら</a>
          </div>


        </div>
      </div>
    </div>

  </div>
</template>


<style lang="scss">
  $sp: 768px; // スマホなど

  @mixin sp {
    @media (max-width: ($sp)) {
      @content;
    }
  }


  .header-catch {
    font-size: 3rem;
    padding-top: 2rem;
    padding-left: 2rem;
  }

  .portfolio__content {
    width: 80%;
    margin: auto;
  }

  .port-content {
    font-size: 1.6rem;
    padding-top: 2rem;
    padding-bottom: 3rem;
  }

  .port__table-of-contents {
    width: 30rem;
    margin-bottom: 5rem;
    padding: 0.8rem;
    background-color: #F5F5F5;
    @include sp{
      width: 100%;
    }
  }

  .table-of-contents__item {
    display: block;
  }

  .port__item {
    width: 100%;
    margin-bottom: 2rem;
  }

  .item__category {
    font-size: 2.4rem;
    font-weight: bold;
    border-bottom: 1px solid #BBBBBB;
  }

  .item__grid {
    margin-top: 2rem;
    display: grid;
    grid-auto-rows: 30rem;
    grid-template-columns: repeat(auto-fill, 24rem);
    grid-row-gap: 2rem;
    grid-column-gap: 2rem;
    justify-content: space-between;
  }

  .card {
    width: 100%;
    height: 100%;
    border-radius: 0.8rem;
    border: 0.1rem solid #DDDDDD;
    position: relative;

    &:hover {
      opacity: 0.5;
    }
  }

  .card__title {
    width: 100%;
    padding-top: 0.8rem;
    padding-left: 0.8rem;
  }

  .card__img {
    width: 100%;
    height: 16rem;
    overflow: hidden;
  }

  .card__discription {
    font-size: 1.2rem;
    padding: 0.8rem;
  }

  .card__link {
    position: absolute;
    right: 0.4rem;
    bottom: 0.4rem;
    ;
  }

</style>
