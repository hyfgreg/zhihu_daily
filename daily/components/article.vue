<template>
    <div class="daily-article">
        <div class="daily-article-title">{{ data.title }}</div>
        <div v-html="data.body" class="daily-article-content"></div>
        <div class="daily-comments" v-show="comments.length">
            <span>评论（{{ comments.length }}）</span>
            <div class="daily-comment" v-for="comment in comments">
                <div class="daily-comment-avatar">
                    <img :src="comment.avatar">
                </div>
                <div class="daily-comment-content">
                    <div class="daily-comment-name">{{ comment.author }}</div>
                    <div class="daily-comment-time" v-time="comment.time"></div>
                    <div class="daily-comment-text">{{ comment.content }}</div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import $ from '../libs/util';
import Time from '../directives/time.js'
export default {
    directives:{
        Time
    },
    props:{
        articleId :{
            type:[String, Number]
        }
    },
    data(){
        return {
            data: {},
            comments : []
        }
    },
    watch:{
        articleId: function(){
            try{
                $.ajax.get('news/'+this.articleId).then(res=>{
                    res.body = res.body.replace(/src="http:/g, 'src="'+ $.apiPath + 'img?img=http:')
                    res.body = res.body.replace(/src="https:/g, 'src="'+ $.apiPath + 'img?img=https:')
                    this.data = res
                    window.scrollTo(0,0);
                });
                
                $.ajax.get('story/'+this.articleId+'/short-comments').then(res=>{
                    res.comments.forEach(element => {
                        element.avatar = $.apiPath + 'img?img=' + element.avatar;
                        this.comments.push(element);
                        // console.log(element.avatar)
                    });
                });
                // console.log(this.comments)
            }
            catch(e){
                this.article = ''
            }
        }
    }
}
</script>

<style>

</style>
