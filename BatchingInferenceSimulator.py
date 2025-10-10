"""
Batching Inference Simulator
Author: Yiru Fang
Description: Simulate batching of inference requests to improve throughput.
"""

class InferenceBatcher:
    def __init__(self, batch_size):
        self. batch_size = batch_size
        self.batch = []
        """
        Initialize the batcher.
        :param batch_size: int, number of requests to group together
        """
        # TODO: init buffer and batch_size
        pass

    def add_request(self, req):
        if len(self.batch)== self.batch_size:
            self.flush()
        self.batch.append(req)
        print(self.batch)

        """
        Add a new request to the batcher.
        :param req: any object representing a request (string, dict, etc.)
        """
        # TODO: append request to buffer
        # TODO: if buffer is full, call flush()
        pass

    def flush(self):
        """
        Process and clear the current batch.
        """
        self.batch=[]
        
        # TODO: process all requests in buffer
        # TODO: reset buffer
        pass


# ===============================
# Example usage (fill after implementation)
# ===============================
if __name__ == "__main__":
    batcher = InferenceBatcher(batch_size=3)
    batcher.add_request("req1")
    batcher.add_request("req2")
    batcher.add_request("req3")  # should trigger flush automatically
    batcher.add_request("req4")
    batcher.flush()  # manually flush remaining requests
