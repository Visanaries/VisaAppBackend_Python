from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('app.conf')
mongo_url = conf.get_string('mongo.url')
