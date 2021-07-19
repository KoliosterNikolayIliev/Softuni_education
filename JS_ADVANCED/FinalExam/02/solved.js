class Story {
    constructor(title, creator) {
        this.title = title;
        this.creator = creator;
        this._comments = [];
        this._likes = [];
    }

    get likes() {
        if (this._likes.length === 0) {
            return `${this.title} has 0 likes`;
        } else if (this._likes.length === 1) {
            return `${this._likes[0]} likes this story!`;
        } else {
            return `${this._likes[0]} and ${this._likes.length - 1} others like this story!`;
        }
    }

    like(username) {
        if(this._likes.includes(username)) {
            throw new Error(`You can't like the same story twice!`);
        }

        if (this.creator == username) {
            throw new Error(`You can't like your own story!`);
        }

        this._likes.push(username);
        return `${username} liked ${this.title}!`;
    }

    dislike(username) {
        if (!this._likes.includes(username)) {
            throw new Error(`You can't dislike this story!`);
        }

        const index = this._likes.indexOf(username);
        if (index > -1) {
            this._likes.splice(index, 1);
        }

        return `${username} disliked ${this.title}`;
    }

    comment(username, content, id) {
        let commentToReply = this._comments.find(c => c.id == id);

        if(!commentToReply) {
            let comment = {
                id: this._comments.length + 1,
                username: username,
                content: content,
                replies: [],
            };

            this._comments.push(comment);

            return `${username} commented on ${this.title}`;
        }

        let reply = {
            id: `${commentToReply.id}.${commentToReply.replies.length + 1}`,
            username: username,
            content: content,
        }

        commentToReply.replies.push(reply);

        return `You replied successfully`;
    }

    toString(sortingType) {
        let result = [];

        result.push(`Title: ${this.title}`);
        result.push(`Creator: ${this.creator}`);
        result.push(`Likes: ${this._likes.length}`);
        result.push(`Comments:`);

        const commentsCopy = this._comments.slice();

        if (sortingType === 'asc') {
            for (const comment of commentsCopy.sort((a,b) => a.id - b.id)) {
                result.push(`-- ${comment.id}. ${comment.username}: ${comment.content}`);

                const repliesCopy = comment.replies.slice();
                for (const reply of repliesCopy.sort((a, b) => a.id.localeCompare(b.id))) {
                    result.push(`--- ${reply.id}. ${reply.username}: ${reply.content}`);
                }
            }
        } else if (sortingType === 'desc') {
            for (const comment of commentsCopy.sort((a,b) => b.id - a.id)) {
                result.push(`-- ${comment.id}. ${comment.username}: ${comment.content}`);

                const repliesCopy = comment.replies.slice();
                for (const reply of repliesCopy.sort((a, b) => b.id - a.id)) {
                    result.push(`--- ${reply.id}. ${reply.username}: ${reply.content}`);
                }
            }
        } else if (sortingType == 'username') {
            for (const comment of commentsCopy.sort((a,b) => a.username.localeCompare(b.username))) {
                result.push(`-- ${comment.id}. ${comment.username}: ${comment.content}`);

                const repliesCopy = comment.replies.slice();
                for (const reply of repliesCopy.sort((a,b) => a.username.localeCompare(b.username))) {
                    result.push(`--- ${reply.id}. ${reply.username}: ${reply.content}`);
                }
            }
        }

        return result.join('\n');
    }
}