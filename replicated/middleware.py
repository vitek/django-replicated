from replicated import routers

class MasterSlaveMiddleware(object):
    def process_request(self, request):
        routers.randomize_slave()
        if request.method == 'POST':
            routers.use_slave(False)
        else:
            routers.use_slave(True)
