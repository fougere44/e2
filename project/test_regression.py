try:
    from app import app
    import unittest

except Exception as e:
    print("Some modules are Missing {}".format(e))


class TestConfig(unittest.TestCase):

    def test_config_loading(self):
        self.assertTrue(app.config['DEBUG'])
        #assert app.config['DEBUG'] is True
        


class FlaskTestCase(unittest.TestCase):

    # Check if response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)


    #Check for data returned
    def test_index_data(self):
        tester = app.test_client(self)
        response = tester.get("/")
        self.assertTrue(b'Predict' in response.data)

   

if __name__ == "__main__":
    unittest.main()
