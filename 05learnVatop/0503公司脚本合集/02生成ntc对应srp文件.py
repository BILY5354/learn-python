# 注意 此脚本生成完毕后 好像unit是需要修改的 结合目录下手动生成的对比一下
# Y:\linzhong\Simulation

import os
from dataclasses import dataclass, field


@dataclass
class Unit:
    block: str
    row: str
    col: str
    fov_id: str
    movement_id: str = field(default='1')

    def __repr__(self):
        return f"{self.movement_id},{self.block},{self.row},{self.col},{self.fov_id}"

    def get_unit_name(self):
        return f"{self.movement_id},{self.block},{self.row},{self.col},{self.fov_id}"


def get_pngs_path(path: str) -> list:
    pngs_path = []

    for dirpath, dirnames, filenames in os.walk(path):
        
        for file in filenames:
            if file.endswith(".png"):
                pngs_path.append(os.path.join(dirpath, file))

    return pngs_path

    """pngs_path[0].split('\\')示例
    [ 
        '', '', '192.168.0.11', 'Data', 'linzhong', 'Simulation', '1112', 
        '1112-1NTC.srp_files', 'MAG0_1', 
        '20231114-66-AE600F25AF154B37B05128F09E7ED59D', 
        'M0F0B0R0C0', 'Sim2.srp_files', 'MAG0_1', 'F1B0r0c0_O0_C1L1.png'
    ]
    """


if __name__ == '__main__':
    """注意生成的路径可能是需要修改的
    #! 具体是哪里还需要去对比确认一下

    Returns:
        _type_: _description_
    """
    pngs_path: list = get_pngs_path(r'\\192.168.0.11\Data\linzhong\Simulation\1124\1124-NTC.srp_files\MAG0_1')

    total_pngs_info: list = []  # 保存所有的图片信息 

    #* 来到新的文件夹修改下面的地址
    for dirpath, dirnames, filenames in os.walk(r'\\192.168.0.11\Data\linzhong\Simulation\1124\1124-NTC.srp_files\MAG0_1'):

        total_frame_id = dirnames
        for i in dirnames:
            total_pngs_info.append({})
        break

    def get_image_path(temp_list: list):
        current_png_name = temp_list[-1]
        current_cam_id = current_png_name[13]
        current_light_id = current_png_name[15]
        return fr'Image:{current_cam_id}*{current_light_id}*{temp_list[-5]}\{temp_list[-4]}\{temp_list[-3]}\{temp_list[-2]}\{temp_list[-1]}'

    for png_path in pngs_path:
        
        current_png_split = png_path.split('\\')
        current_frame_name = current_png_split[-5]  # 当前图片的片名字

        current_frame_id = total_frame_id.index(current_frame_name)  # 对应插入的位置

        if 'Sim1.srp_files' in current_png_split[-3]:
            current_fov_id = '1'
        elif 'Sim2.srp_files' in current_png_split[-3]:
            current_fov_id = '2'
        else:
            print('fovId寻找失败')
            break

        current_row_col = current_png_split[-4]  # 行列式在M0F0B0R0C0 R是行 col是列
        current_unit = Unit(
            block=current_row_col[3],
            row=current_row_col[-3], 
            col=current_row_col[-1], 
            fov_id=current_fov_id
        )

        current_image_path = get_image_path(current_png_split)
        if current_unit.get_unit_name() not in total_pngs_info[current_frame_id]:
            total_pngs_info[current_frame_id][current_unit.get_unit_name()] = []
            total_pngs_info[current_frame_id][current_unit.get_unit_name()].append(current_image_path)
        else:
            total_pngs_info[current_frame_id][current_unit.get_unit_name()].append(current_image_path)


    with open('./out.txt', 'a', encoding='utf8') as f:
        for i, c_frame_dict in enumerate(total_pngs_info):
            f.write(f'\nFrame:{i}\n')

            for c_unit, c_images_list in c_frame_dict.items():
                f.write(f'Unit:{c_unit}\n')
                
                for c_image_path in c_images_list:
                    f.write(f'{c_image_path}\n')
