from epyseri import TridentTraceClient
from rich import print

ttc = TridentTraceClient(
    base_url="https://stg-trident-trace.efishery.com",
    auth_token="edo"
)

# get_health_result = ttc.get_health()
# print(get_health_result)

# get_list_inference_res = ttc.get_list_inference(
#     business_domain="vibrio-vision",
#     limit=3
# )
# print(get_list_inference_res)

# get_detail_inference_res = ttc.get_detail_inference(inference_uuid="273e752e-fb41-488a-9026-ea164440bd1a")
# print(get_detail_inference_res)

# delete_inference_res = ttc.delete_inference(inference_uuid="5c462e22-dad0-46eb-9af8-fb7f34a6cf06")
# print(delete_inference_res)

# get_group_inference_res = ttc.get_group_inference(
#     business_domain = "vibrio-vision",
#     user="string",
#     limit = 1,
#     offset = 0,
# )
# print(get_group_inference_res)

# get_group_detail_inference_res = ttc.get_detail_group_inference(group_id="3LtgvRHgi0M")
# print(get_group_detail_inference_res)

# create_feedback_res = ttc.post_feedback(
#     inference_uuid="74642c5b-c4ad-49f8-b1da-2d482bb424f8", 
#     user_comment={
#         "id": 22,
#         "user": "nama",
#         "message": "Test Mas"
#     }, 
#     user_reaction=True
# )
# print(create_feedback_res)
