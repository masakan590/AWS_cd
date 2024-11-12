from app import db, items

def create_sample_data():
    # ダミーデータを作成
    sample_items = [
        items(name="Item 1", price=1000),
        items(name="Item 2", price=1500),
        items(name="Item 3", price=2000),
        items(name="Item 4", price=2500),
    ]

    # データベースに挿入
    db.session.bulk_save_objects(sample_items)
    db.session.commit()

    print("Sample data has been inserted into the database!")

if __name__ == '__main__':
    # ダミーデータの作成
    create_sample_data()