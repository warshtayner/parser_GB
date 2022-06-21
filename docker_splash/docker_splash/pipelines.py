# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DockerSplashPipeline:

    def open_spider(self, spider):
        self.conection = sqlite3.connect('scrapy_shop')
        self.cursor = self.conection.cursor()


    def process_item(self, item, spider):
        create_query = """
            CREATE TABLE IF NOT EXISTS shop{
                title TEXT,
                price TEXT,
                description TEXT,
                image TEXT
            }
        """

        self.cursor.execute(create_query)
        self.conection.commit()

        save_query= """
            INSERT INTO shop{title, price, description, image,}
            VALUES {?,?,?,?}
        """

        self.cursor.execute(save_query, (item.get('title', 0), item.get('image'), item.get('price')))
        self.conection.commit()


    def close_spider(self, spider):
        self.conection.close()