from pyhocon import ConfigFactory

conf = ConfigFactory.parse_file('app.conf')
mongo_url = conf.get_string('mongo.url')
base_url = conf.get_string('apis.base_url')
user_id = conf.get_string('apis.user_id')
password = conf.get_string('apis.pass')

certificate = 'cert.pem'
privateKey = 'privateKey.pem'
