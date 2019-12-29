# -*- coding:utf-8 -*-
import numpy as np
import jieba

from wordcloud import WordCloud
from matplotlib import pyplot as plt
from PIL import Image


def generate_word_cloud(text, image_name='picture.jpg', generate_picture_name='sample.jpg'):
    """
    读取文本信息生成词云图
    :param text: 词云文本
    :param image_name: 词云背景图片
    :param generate_picture_name: 生成图片的名称
    :return:
    """
    img = Image.open(image_name)  # 打开本地图片
    img_array = np.array(img)  # 将图片装换为数组
    font = r'C:\Windows\Fonts\FZSTK.TTF'
    wc = WordCloud(background_color='white',
                   width=1000,
                   height=800,
                   mask=img_array,  # 根据图片背景框来填充词云
                   font_path=font,  # 如果是中文必须要添加这个，否则会显示成框框
                   )

    # 构建普通词云文本
    # wc.generate(text)

    # 使用分词构建词云文本
    cut = jieba.cut(text)
    string = ' '.join(cut)
    wc.generate_from_text(string)

    # 运行结束后预览图片
    plt.imshow(wc)  # 用plt显示图片
    plt.axis('off')  # 不显示坐标轴
    plt.figure()
    plt.show()  # 显示图片
    # wc.to_file(generate_picture_name)  # 保存词云图片到本地


if __name__ == '__main__':
    long_text = """
    The Positive Meanings of Love
    We'd like to share some of the positive meanings love has for us.
    Love means that I know the person I love. I'm aware of the many sides of the other person - not just the beautiful side but also the limitations, inconsistencies and faults. I have an awareness of the other's feelings and thoughts, and I experience something of the core of that person. I can penetrate social masks and roles and see the other person on a deeper level.
    Love means that I care about the welfare of the person I love. To the extent that it is genuine, my caring is not possessive, nor does it hold the other person back. On the contrary, my caring frees both of us. If I care about you, I'm concerned about your growth, and I hope you will become all that you can become. Consequently, I don't put up obstacles to what you do that enhances you as a person, even though it may result in my discomfort at times.
    Love means having respect for the dignity of the person I love. If I love you, I can see you as a separate person, with your own values and thoughts and feelings, and I do not insist that you surrender your identity to match an image of what I expect you to be for me. I can allow and encourage you to stand alone and to be who you are, and I avoid treating you as an object or using you primarily to satisfy my own needs.
    Love means having a responsibility toward the person I love. If I love you, I respond to most of your major needs as a person. This responsibility does not include my doing for you what you are capable of doing for yourself; nor does it mean that I run your life for you. It does mean acknowledging that what I am and what I do affects you, so that I am directly involved in your happiness and your suffering. A lover does have the capacity to hurt or ignore the loved one, and in this sense we see that love involves an acceptance of some responsibility for the impact my way of being has on you.
    Love means making a commitment to the person I love. This commitment does not mean surrendering our total selves to each other; nor does it imply that the relationship is necessarily permanent. It does involve a willingness to stay with each other in times of pain, struggle, and despair, as well as in times of calm and enjoyment.
    Love means trusting the person I love. If I love you, I trust that you will accept my caring and my love and that you won't deliberately hurt me. I trust that you will find me attractive, and that you won't abandon me; I trust the mutual nature of our love. If we trust each other, we are willing to be open to each other and reveal our true selves.
    Love can tolerate imperfection. In a love relationship there are times when I am bored, times when I may feel like giving up, times of real strain, and times I feel I can't move forward. Authentic love does not imply enduring happiness. I can stay during rough times, however, because I can remember what we had together in the past, and I can picture what we will have together in our future if we care enough to face our problems and work them through. We agree with the idea that love is a spirit that changes life. Love is a way of life that is creative and that transforms. However, love is not reserved for a perfect world. Love is meant for our imperfect world where things go wrong. Love is meant to be a spirit that works in painful situations. Love is meant to bring meaning into life where nonsense appears to rule. In other words, love comes into an imperfect world to make it possible to live.
    Love is open. If I love you, I encourage you to reach out and develop other relationships. Although our love for each other and our commitment to each other might prohibit certain actions on our parts, we are not totally and exclusively married to each other. It is a false love that cements one person to another in such a way that he or she is not given room to grow.
    Love is selfish. I can only love you if I genuinely love, value, appreciate, and respect myself. If I am empty, then all I can give you is my emptiness. If I feel that I'm complete and worthwhile in myself, then I'm able to give to you out of my fullness. One of the best ways for me to give you love is by fully enjoying myself with you.
    Love involves seeing the potential within the person we love. In my love for another, I view her or him as the person she or he can become, while still accepting who and what the person is now. By taking people as they are, we make them worse, but by treating them as if they already were what they ought to be, we help make them better.
    To sum it up, mature love is union under the condition of preserving one's individuality. In love, two beings become one and yet remain two.
    """
    generate_word_cloud(text=long_text)