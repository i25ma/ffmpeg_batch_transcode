import os
import multiprocessing


def compress_videos(input_dir, output_dir):
    # 创建输出目录
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 检查输入目录是否存在
    if not os.path.exists(input_dir):
        os.mkdir(input_dir)
    
    # 手动设置两个进程处理视频压缩任务
    pool = multiprocessing.Pool(2)

    # 遍历输入目录的文件
    files = os.listdir(input_dir)
    if len(files) > 0:
        for filename in files:
            if filename.endswith('.mp4'):
                input_file = os.path.join(input_dir, filename)
                output_file = os.path.join(output_dir, filename)
                print('开始处理视频...')
                pool.apply_async(run_func, args=(input_file, output_file))
    else :
        print('input_dir 文件数为： {} 个，任务停止执行！'.format(len(files)))
        return 0

    pool.close()
    pool.join()
    print('全部视频已处理完成！')
        
# CRF 参数说明
# 范围：CRF 的取值范围通常是 0 到 51。
# 0：无损编码，质量最高，但文件大小会非常大。
# 18-24：常用的范围。18 通常被认为是视觉上无损，而 23-24 是较为常见的默认设置。
# 28-30：较低质量，适用于对文件大小有严格要求的场合。
# 质量与文件大小关系：降低 CRF 值会提高视频质量，但会增加文件大小；提高 CRF 值则会降低质量并减少文件大小。

# preset 参数说明
# preset: 是一个编码参数，决定了编码的速度和文件大小/质量的平衡。不同的 preset 有不同的设置，影响编码速度和压缩效果。
# placebo:
# 是 libx265 的预设中最慢的选项。使用这个选项时，编码会尽可能地优化文件大小和质量，但编码速度非常慢，CPU 使用率可能较高。
# 适合对质量要求极高并且不在意编码时间的场景。
# 常用的 preset
# ultrafast: 编码速度最快，文件较大，质量最差。
# superfast: 快速，适度牺牲质量。
# veryfast: 比较快，通常是常用选项。
# faster: 快于快速
# fast
# medium: 默认设置，速度和质量的平衡。
# slow: 提供较好质量，编码速度更慢。
# veryslow: 质量进一步提升，但编码时间显著增加。
# placebo: 最慢但质量和压缩最优。


def run_func(input_file, output_file):
    os.system("ffmpeg -i {} -c:v libx265 -x265-params crf=18:preset=placebo {}".format(input_file, output_file))

if __name__ == '__main__':
    input_directory = './input'  # 替换为你的输入目录
    output_directory = './output'  # 替换为你的输出目录
    compress_videos(input_directory, output_directory)