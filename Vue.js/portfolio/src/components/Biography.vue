<template>

  <div class="biography">
    <div class="biography__header">
      <div class="header-catch">Biography</div>
    </div>
    <div class="biography__content bio-content">

      <div class="bio-name">
        Programmer<br><br>
        <div class="name-text">小林 秀樹<br></div>
        Hideki Kobayashi<br><br>
      </div>

      <div class="bio-list">
        <div>1995年</div>
        <div>東京都生まれ<br></div>
        <div>2013年</div>
        <div>東洋大学理工学部電気電子情報工学科入学。<br>C言語、html/cssに出会う。<br></div>
        <div>2016年</div>
        <div>立教大学経営学部入学。<br>学生団体のwebページ制作を行う。<br></div>
        <div>2017年</div>
        <div>Life is TechのAndroidメンターとして活動<br>
          Pythonを学び始める。
        </div>
        <div>2018年</div>
        <div>Python/Djangoの講師として活動。<br>
          UdemyのPython/Django講座の講師も担当。→<a href="https://www.udemy.com/pythondjango-p/">Udemy講座はこちら</a><br>
          フリーでwebページの受託開発も行う。</div>
      </div>

      <div class="bio-text">
        2016年から仕事として様々なプロジェクトにエンジニアとして参画。開発だけでなく、教育に関心がある。日本のIT教育の遅さに危機感を覚え、また現状のIT教育サービスの不誠実さ、不十分さにも不満を持ち自分でサービスを作ろうと決意。初心者から仕事ができるところまでサポートができるようにしたい。そのために自分の技術を確たるものにするため日々精進。
      </div>

    </div>
  </div>

</template>

<script></script>


<style lang="scss">
  $sp: 768px; // スマホなど

  @mixin sp {
    @media (max-width: ($sp)) {
      @content;
    }
  }

  .biography {
    width: 100%;
    padding-bottom: 7.2rem;
    
    
  }

  .header-catch {
    font-size: 3rem;
    padding-top: 2rem;
    padding-left: 2rem;
  }

  .biography__content {
    width: 80%;
    margin: auto;
    margin-top: 5rem;
  }

  .bio-content {
    font-size: 1.6rem;
    padding-top: 2rem;
    
    @include sp{
      font-size: 1rem;
    }
  }

  .name-text {
    font-size: 2rem;
    @include sp{
      font-size: 1.6rem;
    }
  }

  .bio-list {
    display: grid;
    grid-template-columns: 6.4rem 1fr;
  }

  .bio-text {
    margin-top: 4.8rem;
  }

</style>
