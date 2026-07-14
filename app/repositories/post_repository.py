from sqlalchemy.orm import Session, joinedload

from app.models.place import Place
from app.models.post import Post
from app.models.post_image import PostImage


class PostRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_place(self, place_id: int) -> Place | None:
        return self.db.get(Place, place_id)

    def get_post(self, post_id: int) -> Post | None:
        return self.db.query(Post).options(joinedload(Post.images)).filter(Post.id == post_id).first()

    def list_posts(self, place_id: int | None) -> list[Post]:
        query = self.db.query(Post).options(joinedload(Post.images)).order_by(Post.id.desc())
        if place_id is not None:
            query = query.filter(Post.place_id == place_id)
        return query.all()

    def get_image(self, image_id: int) -> PostImage | None:
        return self.db.get(PostImage, image_id)

    def save(self, post: Post) -> Post:
        self.db.add(post)
        self.db.commit()
        self.db.refresh(post)
        return post

    def delete(self, post: Post) -> None:
        self.db.delete(post)
        self.db.commit()
