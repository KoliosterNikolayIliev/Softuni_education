function solve() {
    class Post {
        constructor(title, content) {
            this.title = title;
            this.content = content;
        }

        toString() {
            return `Post: ${this.title}\nContent: ${this.content}`;

        }
    }

    class SocialMediaPost extends Post {
        constructor(title, content, likes, dislikes) {
            super(title, content);
            this.comments = [];
            this.likes = likes;
            this.dislikes = dislikes;
        }

        addComment(comment) {
            this.comments.push(comment);
        }

        toString() {
            let commentStr = this.comments.length>0?`Comments:\n${this.comments.map(comment => ` * ${comment}`).join('\n')}`:'';
            let result =  super.toString();
            let rating = `Rating: ${this.likes - this.dislikes}`
            return [result,rating,commentStr].join('\n').trim();

        }
    }

    class BlogPost extends Post {
        constructor(title, content, views) {
            super(title, content);
            this.views = views;
        }

        view() {
            this.views++;
            return this;
        }

        toString() {
            return super.toString() + `\nViews: ${this.views}`;

        }
    }

    return {
        Post,
        SocialMediaPost,
        BlogPost,
    };
}

