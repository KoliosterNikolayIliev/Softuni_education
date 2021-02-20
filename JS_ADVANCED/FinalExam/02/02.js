class Story {
    constructor(title, creator) {
        this.title = title
        this.creator = creator
        this._comments = []
        this._likes = []


    }
    get likes (){
        if(this._likes.length ===0) {
            return `${this.title} has 0 likes`
        }
        if (this._likes.length ===1) {
            return `${this._likes[0].username} likes this story!`
        } else {
            return `${this._likes[0].username} and ${this._likes.length-1} others like this story!`
        }

    }
    like (username){
        let like = this._likes.find(like=>like.username === username)
        if (like!==undefined) {
            return "You can't like the same story twice!"
        }
        if (username === this.creator) {
            return "You can't like your own story!"
        }
        this._likes.push({username:username,title:this.title})
        return `${username} liked ${this.title}!`
    }
    dislike (username){
        let like = this._likes.find(like=>like.username === username)
        if (like===undefined) {
            throw new Error ("You can't dislike this story!")
        }
        this._likes.splice(this._likes.indexOf(like),1)
        return `${username} disliked ${this.title}`
    }
    comment (username, content, id){
        let comment = this._comments.find(comment=>comment.id===id)
        if (id === undefined || comment===undefined){
            if (id){
                comment = {id:id,username:username,content:content,replies:[]}
                this._comments.push(comment)
            }else{
                if (this._comments.length>0){
                    id = this._comments[this._comments.length-1]+1
                    comment = {id:id,username:username,content:content, replies:[]}
                    this._comments.push(comment)
                }else{
                    id = 1
                    comment = {id:id,username:username,content:content,replies:[]}
                    this._comments.push(comment)
                }
            }
            return `${username} commented on ${this.title}`
        }else{

            let sdigit = comment.replies.length
            let repId = Number(id.toString()+'.'+sdigit.toString())
            comment.replies.push({id:repId,username:username,content:content})
            return `${username} commented on ${this.title}`
        }


    }
    toString (sortingType){

    }
}


let art = new Story("My Story", "Anny");
art.like("John");
console.log(art.likes);
art.dislike("John");
console.log(art.likes);
// art.comment("Sammy", "Some Content");
// console.log(art.comment("Ammy", "New Content"));
// art.comment("Zane", "Reply", 1);
// art.comment("Jessy", "Nice :)");
// console.log(art.comment("SAmmy", "Reply@", 1));
// console.log()
// console.log(art.toString('username'));
// console.log()
// art.like("Zane");
// console.log(art.toString('desc'));

// John likes this story!
//     My Story has 0 likes
// Ammy commented on My Story
// You replied successfully
//
// Title: My Story
// Creator: Anny
// Likes: 0
// Comments:
//     -- 2. Ammy: New Content
// -- 3. Jessy: Nice :)
// -- 1. Sammy: Some Content
// --- 1.2. SAmmy: Reply@
// --- 1.1. Zane: Reply
//
// Title: My Story
// Creator: Anny
// Likes: 1
// Comments:
//     -- 3. Jessy: Nice :)
// -- 2. Ammy: New Content
// -- 1. Sammy: Some Content
// --- 1.2. SAmmy: Reply@
// --- 1.1. Zane: Reply

