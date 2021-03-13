from PIL import Image, ImageDraw
import json
import time


class AntiAliasing:
    def __init__(self, output_file_name: str, width: int, height: int, round_: int, multiple: int, color: list):
        if color is None:
            color = [0, 0, 0, 255]
        self.output_file_name = output_file_name
        self.width = width
        self.height = height
        self.round = round_
        self.multiple = multiple
        self.color = color

        self.im = Image.new("RGBA", (self.width * self.multiple, self.height * self.multiple))

        self.draw_round_rec(tuple(self.color), 0, 0, self.width * self.multiple, self.height * self.multiple,
                            self.round * self.multiple)

        self.smaller(self.width, self.height)

        self.im.save(self.output_file_name, format="PNG")

    def smaller(self, width, height):
        originPixels = self.get_pixels()
        vt = int(self.im.height / height)
        ht = int(self.im.width / width)
        output = []

        for y in range(height):
            for x in range(width):
                output.append(tuple(self.get_average_alpha(originPixels, self.color, x, y, vt, ht)))
        self.im = Image.new("RGBA", (width, height))
        self.im.format = "PNG"
        self.im.putdata(output)

    def get_average_alpha(self, pixels, color, x, y, vt, ht):
        xh = x * ht
        yv = y * vt
        sum_ = 0
        for row in pixels[yv:yv + vt]:
            for col in row[xh:xh + ht]:
                sum_ += col[3]
        color[3] = int(sum_ / (vt * ht))
        return color

    def get_pixels(self):
        imagePixels = []
        x = 0
        oneRow = []
        for data in self.im.getdata():
            if x == self.im.width:
                imagePixels.append(oneRow)
                oneRow = []
                x = 0
            oneRow.append(data)
            x += 1
        imagePixels.append(oneRow)
        return imagePixels

    def draw_round_rec(self, color, x, y, w, h, r):
        drawObject = ImageDraw.Draw(self.im)
        w = w - 1
        h = h - 1

        drawObject.polygon([(x + r, y), (x + r, y + r), (x, y + r),
                            (x, h - r), (x + r, h - r), (x + r, h),
                            (w - r, h), (w - r, h - r), (w, h - r),
                            (w, y + r), (w - r, y + r), (w - r, y)], fill=color)

        r = r * 2
        drawObject.ellipse([(x, y), (x + r, y + r)], fill=color)
        drawObject.ellipse([(w - r, y), (w, y + r)], fill=color)
        drawObject.ellipse([(x, h - r), (x + r, h)], fill=color)
        drawObject.ellipse([(w - r, h - r), (w, h)], fill=color)


if __name__ == "__main__":
    with open("data.json", mode="r", encoding="utf-8") as f:
        dataStr = f.read()
        dataJson = json.loads(dataStr)
        for data in dataJson:
            start = time.time_ns()
            antiAliasing = AntiAliasing(data["name"] + ".png", data["width"], data["height"], data["round"], 4,
                                        data["color"])
            end = time.time_ns()
            ms = (end-start)/1000/1000
            print(data["name"] + " finished. {:.4f}s or {:.4f}ms".format(ms/1000, ms))

