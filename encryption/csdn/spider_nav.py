import re
import os
import requests


if __name__ == '__main__':
    # 我加入的社区肯定要每个用户都不一样的，所以需要登录（cookie
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
        'Cookie': 'uuid_tt_dd=10_18853603210-1680152514986-783151; c_adb=1; pixelhecomment_new=1705462247593; cf_clearance=RhFHerugKfVmPrBmvsKaTNDOB_g.vX0gEQK17i2Db98-1711906562-1.0.1.1-ky7Vza7yV2TrRLJzbO9sEGD.2RaoUOgHruUt2lRCC3r3PnRUCRFMiyDN_ZDqD1mRth3Oyu.x_VDadsTfcCP1kA; historyList-new=%5B%5D; c_dl_prid=1711906680308_471825; c_dl_rid=1711906722489_471355; c_dl_fref=https://so.csdn.net/so/search; c_dl_fpage=/download/zzjlhlcd/85656672; c_dl_um=distribute.pc_relevant_download.none-task-download-2%7Edefault%7ELANDING_RERANK%7ERate-1-19408265-download-10962106.257%5Ev14%5Epc_dl_relevant_base1_a; loginbox_strategy=%7B%22taskId%22%3A317%2C%22abCheckTime%22%3A1711945147481%2C%22version%22%3A%22ExpA%22%2C%22nickName%22%3A%22pixelhe%22%2C%22blog-threeH-dialog-expa%22%3A1711905732186%7D; UserName=2401_83556130; UserInfo=24c309fa5b2d4a22a424fb9c894fab63; UserToken=24c309fa5b2d4a22a424fb9c894fab63; UserNick=%E5%AD%A6%E9%9C%B8%E9%A3%9E%E9%A3%9E5; AU=06D; UN=2401_83556130; BT=1711945188278; p_uid=U110000; dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTExMDg3NiwiZXhwIjoxNzEyNTQ5OTk1LCJpYXQiOjE3MTE5NDUxOTUsInVzZXJuYW1lIjoiMjQwMV84MzU1NjEzMCJ9._VasKBw7nH61JNX_mf7dAOaYrgvjSQ6DcUuFdGztgs0; ssxmod_itna=iqGhY5BK0IxmorDz=D2YLE8ZDfgHxQTRvmuDKDsa1bDSxGKidDqxBmmlDDtTtetSi7H+W4qhOihW5Qj8iAxEFjLTfGTpn4iTD4q07Db4GkDAqiOD7TRtoD4RKGwD0eG+DD4DWCqDt/ENqDFUqtS0kLu3LLnUqDEtkQDYMQDmLbDnhiVDlU6f7iDf8QDIwXu/4GnD0QWNdRMD0f35PaDzkQDbopBf6FDtwTR/4DHnLXVtqHo4hGW7F4s8u3rf7vq3YmK0A8PCAvLyIhPASGiiS+oi5DACDEnPD===; ssxmod_itna2=iqGhY5BK0IxmorDz=D2YLE8ZDfgHxQTRvmuDikAaYqDl=jCDj42QM2LuZUTvL6=yFDCIw1OCxAp3ybBCg4wnbfm3a+QsSi8c3Yq=CEAk1GRnKDCUpzCTmV7FMQbA94bAb2G2kfeO4wOushgpsh7FPOg0GqjFYXlyGiz9Du0ebOPKTLpx3DQKxUD08DYKx4D=; firstDie=1; dc_sid=f9375c46a6486d16edea87215563552b; c_segment=15; csrfToken=7zhI99Hgq8NSiG88JnMljkHb; c_first_ref=default; fe_request_id=1712045636248_4241_0562501; c_utm_source=csdn_toolbar_xuexi; log_Id_click=481; dc_session_id=10_1712068765202.540789; c_pref=default; c_ref=default; c_first_page=https%3A//bbs.csdn.net/forums/ITID%3Fcategory%3D4; c_dsid=11_1712068765455.528581; c_page_id=default; dc_tos=sbbkpp; log_Id_pv=709; creativeSetApiNew=%7B%22toolbarImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20231011044944.png%22%2C%22publishSuccessImg%22%3A%22https%3A//img-home.csdnimg.cn/images/20240229024608.png%22%2C%22articleNum%22%3A0%2C%22type%22%3A0%2C%22oldUser%22%3Afalse%2C%22useSeven%22%3Atrue%2C%22oldFullVersion%22%3Afalse%2C%22userName%22%3A%222401_83556130%22%7D; log_Id_view=16999'
    }
    resp = requests.get('https://bbs.csdn.net/forums/ITID?category=4', headers=headers)
    if resp.status_code == 200:
        # 获取到html文本
        data = resp.text

        # 不做区分处理：提取官方推荐社区和已加入的社区
        # _re = re.compile(r'"communityHomePage":\s*("[^"]+")')
        # urls = _re.findall(data)
        # print(urls)

        # 做区分处理（分别提取
        # 1、加入的社区提取
        _re_my_community = re.compile(r'"myCommunity":\s*{\s*.*?"default2014LiveRoom')
        my_community_text = _re_my_community.search(data).group(0)
        _re = re.compile(r'"communityHomePage":\s*("[^"]+")')
        urls_my_community = _re.findall(my_community_text)
        # print(my_community_text)
        # 2、推荐社区提取
        _re_recommand = re.compile(r'"recomendCommunitys":\s*{\s*.*"other')
        recommand_community_text = _re_recommand.search(data).group(0)
        _re = re.compile(r'"communityHomePage":\s*("[^"]+")')
        urls_recommand_community = _re.findall(recommand_community_text)

        # 存储到文件
        base_path_recommand_community = os.path.join(os.getcwd(), 'url_nav_recommend.txt')
        base_path_my_community = os.path.join(os.getcwd(), 'url_nav_my_community.txt')

        # 清空文件
        if os.path.exists(base_path_recommand_community):
            os.remove(base_path_recommand_community)
        if os.path.exists(base_path_my_community):
            os.remove(base_path_my_community)

        # 替换转义字符并存储
        with open(base_path_recommand_community, 'w') as f:
            for url in urls_recommand_community:
                url = url.replace('\\u002F', '/')
                # print(url)
                f.write(url + '\n')

        with open(base_path_my_community, 'w') as f:
            for url in urls_my_community:
                url = url.replace('\\u002F', '/')
                # print(url)
                f.write(url + '\n')

