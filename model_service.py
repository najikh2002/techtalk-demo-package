from epyseri import TridentTraceClient
from rich import print
import cv2

# ttc = TridentTraceClient(
#     base_url="https://stg-trident-trace.efishery.com",
#     app_name="test lagi dung",
#     auth_token="edo"
# )

# print(ttc.service_domain_id, ttc.service_domain_slug)

# tanpa image
# post_inference_res = ttc.post_inference(
#         data_input = "coba dung",
#         data_output = "lagi dung",
#         inference_time = 0,
#         business_domain = "Model",
#         ai_domain = "string",
#         ai_subdomain = "string",
#         model_version = "string",
#         group_id = "string",
#         user = "test"
# )
# print(post_inference_res)

# menggunakan image
# image = cv2.imread("./image.png")

# post_inference_res = ttc.post_inference(
#         data_input = {
#                         "public_url": "https://public-tools.s3.ap-southeast-1.amazonaws.com/aiot/mlai/trident-trace/pond-segmentation-lele-terbang/stg/ee0e55e747064d709a2bf3de1610b1ff_input.jpg",
#                         "key": "aiot/mlai/trident-trace/pond-segmentation-lele-terbang/stg/ee0e55e747064d709a2bf3de1610b1ff_input.jpg",
#                         "bucket": "public-tools"
#                     },
#         data_output = {
#                         "predict_result": {
#                             "public_url": "https://public-tools.s3.ap-southeast-1.amazonaws.com/aiot/mlai/trident-trace/pond-segmentation-lele-terbang/stg/ee0e55e747064d709a2bf3de1610b1ff_result.json",
#                             "key": "aiot/mlai/trident-trace/pond-segmentation-lele-terbang/stg/ee0e55e747064d709a2bf3de1610b1ff_result.json",
#                             "bucket": "public-tools"
#                         },
#                         "image_annotated": {
#                             "public_url": "https://public-tools.s3.ap-southeast-1.amazonaws.com/aiot/mlai/trident-trace/pond-segmentation-lele-terbang/stg/ee0e55e747064d709a2bf3de1610b1ff_result.jpg",
#                             "key": "aiot/mlai/trident-trace/pond-segmentation-lele-terbang/stg/ee0e55e747064d709a2bf3de1610b1ff_result.jpg",
#                             "bucket": "public-tools"
#                         }
#                         },
#         inference_time = 0,
#         business_domain = "Healthcare",
#         ai_domain = "string",
#         ai_subdomain = "string",
#         model_version = "string",
#         group_id = "string",
#         user = "test",
#         image = image,
# )
# print(post_inference_res)