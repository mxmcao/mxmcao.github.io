# 个人网站头像生成指南

## 1. 目标与结论

本指南用于把现有真人头像转换为适合当前 Hugo Terminal 学术主页的方形头像。网站的视觉核心是终端界面、等宽字体、硬边框和克制的学术表达，因此头像应同时满足：

- 在约 `220 x 220 px` 的显示尺寸下仍能立即辨认本人；
- 与终端式页面形成统一的高对比、硬边、低噪声视觉；
- 保持严肃、好奇、可信且易接近的研究者气质；
- 只使用黑、白和中性灰，不使用任何有色相的点缀；
- 不借用奖项、机构或品牌的标识来制造身份暗示。

综合所有方案，首选为 **方案 7：现代学术档案雕刻**。它兼具科学家传记的学术感、Terminal 网站所需的高对比度，以及小尺寸头像所需的面部辨识度。若希望头像更直接融入默认深色页面，则选择 **方案 8：深色学术雕刻**。

## 2. 输入素材

### 首选身份参考

- `prev-information/avatar/avatar-1.png`
- 正面构图，面部、眼镜和发型细节清楚，应作为 `Image 1: edit target and identity reference`。

### 可选构图参考

- `prev-information/avatar/avatar-2.png`
- 三分之二侧面构图，可用于探索更具编辑感的版本；它不是首选身份锚点，不应覆盖正面版本。

实际生成时，优先只上传 `avatar-1.png`。若使用两张图片，必须明确：Image 1 决定人物身份，Image 2 只提供侧面姿态或裁切参考，不能混合两张图的面部结构。

## 3. 所有方案共用的硬性约束

以下约束需要原样保留在每次生成和后续迭代中：

1. 任务类型为 style transfer，只改变视觉媒介和渲染方式。
2. 严格保留面部结构、脸型比例、发型轮廓、眼镜几何、眼睛、表情、视线和头部角度。
3. 使用 `1:1` 方形构图，头肩像居中，头发四周留出安全边距，不裁切头顶。
4. 头像缩小到 `220 x 220 px` 后，双眼、镜框、鼻梁、嘴部和发型仍需清楚。
5. 严格采用无色相单色灰阶：纯黑、纯白和中性灰；图像整体 saturation 为 0。
6. 不使用彩色反光、彩边、色调分离、霓虹、发光效果或有色渐变。
7. 不添加文字、姓名、日期、奖章、月桂、Logo、机构标识、终端 UI、边框或水印。
8. 不改变服装时代、年龄、性别表达、种族特征或人物气质。
9. 不把人物泛化成历史名人、虚构科学家、动漫角色或通用商业头像。
10. 眼睛区域保持干净，不允许网点、排线或纹理遮挡瞳孔和镜片。

## 4. 统一基础 Prompt

下面的基础段应放在每个风格 prompt 的开头。后面的各方案只替换 `Primary request`、`Style/medium`、`Scene/backdrop` 和少量媒介约束。

```text
Use case: style-transfer
Asset type: square portrait for a terminal-themed academic personal website
Input images: Image 1 is the edit target and primary identity reference.

Subject: Preserve the person's exact identity, facial structure, facial proportions, hairstyle silhouette, glasses geometry, expression, gaze, head angle, and head-and-shoulders framing from Image 1. The person must remain immediately recognizable when the result is displayed at 220 x 220 pixels.

Composition/framing: Square 1:1 portrait, centered, with comfortable margin around the hair, a clean outer silhouette, and no crop through the top of the head.

Color palette: Strict achromatic monochrome only: pure black, pure white, and neutral gray. Overall saturation must be zero. No chromatic accents, colored reflections, color fringing, split toning, glow, or colored gradients.

Constraints: Change only the visual rendering style. Preserve identity with high fidelity. Keep both eyes clear, the glasses geometrically accurate, and the hairstyle distinct. Maintain strong readability at small avatar size. No text, name, date, medal, laurel wreath, logo, organization mark, terminal UI, decorative frame, or watermark.

Avoid: altered face shape, altered hairstyle, distorted glasses, hidden eyes, beautification that changes identity, generic stock portrait, anime, caricature, childish cartoon styling, excessive background detail, noisy texture across the eyes, and any non-achromatic color.
```

## 5. 设计方案

### 方案 1：技术杂志线描

**定位：** 最稳妥的现代编辑插画，技术感强、细节清楚，适合希望头像不显复古的版本。

```text
Primary request: Transform the portrait into a refined monochrome editorial line portrait for a serious computing and research publication.

Scene/backdrop: Plain white or very light neutral-gray background with no visible objects.

Style/medium: Precise black-ink technical line drawing with controlled contour weight, sparse parallel hatching, crisp facial landmarks, and clean negative space. Contemporary editorial illustration, rigorous and understated rather than decorative.

Lighting/mood: Calm, analytical, curious, credible, and approachable.

Additional constraints: Use line density only where it helps describe facial volume. Keep the eye and lens areas mostly open. Do not imitate a specific publication or living illustrator.
```

### 方案 2：单色丝网印刷

**定位：** 图形感最强，适合更大胆的主页头像；需要控制阴影，避免脸部被压成大黑块。

```text
Primary request: Transform the portrait into a high-contrast monochrome screen-print portrait with a strong, recognizable silhouette.

Scene/backdrop: Flat white background without texture.

Style/medium: One-ink screen printing using solid black, white negative space, and a limited set of neutral-gray halftone values. Hard edges, clean registration, restrained dot pattern, and no distressed poster effects.

Lighting/mood: Direct, intelligent, self-possessed, and contemporary.

Additional constraints: Preserve enough midtone information around the eyes, nose, mouth, and glasses to retain identity. Keep halftone dots fine enough to remain coherent after downscaling.

Avoid: propaganda-poster composition, oversized shadows covering the eyes, torn-paper texture, ink splashes, and faux printing defects.
```

### 方案 3：极简钢笔简笔画

**定位：** 最轻、最亲和，适合偏个人化的表达；线条必须克制，不能变成可爱卡通。

```text
Primary request: Transform the portrait into a minimal monochrome pen portrait using the fewest lines necessary to preserve identity.

Scene/backdrop: Pure white background with generous negative space.

Style/medium: Elegant black fineliner drawing with economical contours, a few deliberate hatch marks, stable line weight, and no filled decorative shapes. Minimal but anatomically observant.

Lighting/mood: Thoughtful, open, precise, and quietly friendly.

Additional constraints: Retain the distinctive hairstyle outline, rectangular glasses, eye placement, nose, and mouth. Simplicity must not reduce the person to a generic icon.

Avoid: doodle style, mascot design, exaggerated head proportions, chibi features, continuous-line gimmicks, and loose unfinished sketch marks.
```

### 方案 4：终端抖动像素肖像

**定位：** 与 Terminal 主题关联最直接，个性鲜明；适合作为备选头像或 favicon 延展，不是正式学术头像的第一选择。

```text
Primary request: Transform the portrait into a crisp monochrome dithered pixel portrait suitable for a terminal-themed academic website.

Scene/backdrop: Solid black or solid white background, selected for the clearest silhouette.

Style/medium: Deliberate pixel art with a restrained grayscale ramp, ordered dithering, square pixels, sharp edges, and no antialiasing. The result should feel like a carefully authored high-resolution terminal portrait rather than a low-quality image conversion.

Lighting/mood: Focused, technical, composed, and intelligent.

Additional constraints: Preserve the exact glasses shape and hairstyle mass. Use enough pixel resolution for both eyes and the mouth to remain distinct at 220 x 220 pixels.

Avoid: retro game character styling, scanlines, CRT curvature, glitch displacement, code text, UI windows, blocky facial distortion, and random compression artifacts.
```

### 方案 5：木刻与版画肖像

**定位：** 质感最强、最具手工气息，能形成醒目的黑白焦点；需要避免过度戏剧化和年代错置。

```text
Primary request: Transform the portrait into a refined monochrome woodcut portrait for a contemporary academic biography.

Scene/backdrop: Plain white or pale neutral-gray field with no scenery.

Style/medium: Controlled relief-print linework, carved black shapes, directional hatch marks, and clear white negative space. Detailed around the face and glasses, simplified around clothing and background.

Lighting/mood: Serious, inquisitive, grounded, and timeless.

Additional constraints: Keep carving marks narrow and purposeful. Preserve smooth identity cues rather than aging the subject or making the face rugged.

Avoid: medieval costume, religious iconography, heroic propaganda, heavy weathering, distressed paper, oversized black eye sockets, and ornamental borders.
```

### 方案 6：纯灰阶编辑摄影

**定位：** 最保守、最真实，适合重视职业可信度和身份保真度的版本；不做插画化处理。

```text
Primary request: Convert the portrait into a polished but natural monochrome editorial headshot for an academic personal website.

Scene/backdrop: Smooth neutral-gray studio background with no gradient hue and no visible objects.

Style/medium: Realistic black-and-white editorial photography with natural skin texture, controlled tonal range, restrained local contrast, and subtle monochrome film grain.

Lighting/mood: Soft directional studio light, calm, credible, attentive, and approachable.

Additional constraints: Preserve real skin texture and the original facial proportions. Remove any chromatic lens reflections without changing the glasses. Keep retouching minimal and invisible.

Avoid: glamour retouching, plastic skin, dramatic movie lighting, crushed shadows, artificial catchlights, beauty reshaping, shallow focus across the eyes, and faux vintage damage.
```

### 方案 7：现代学术档案雕刻（首选）

**定位：** 综合推荐。以十九世纪科学传记插图的铜版与点刻语言为基础，用现代编辑设计控制复杂度。它表达的是“学术档案感”，不复制任何奖项或机构的官方视觉。

```text
Primary request: Transform the portrait into a refined academic archival engraving inspired by nineteenth-century scientific biography illustrations and contemporary editorial portraiture, while remaining original and institution-neutral.

Scene/backdrop: Plain white or very light neutral-gray archival-paper surface with extremely subtle, achromatic paper grain.

Style/medium: Fine copperplate engraving and stipple illustration. Precise black-ink contours, controlled cross-hatching, delicate dot-based tonal shading, and clean modern negative space. Scholarly and restrained rather than theatrical or excessively antique.

Lighting/mood: Calm, serious, curious, academically credible, and approachable.

Additional constraints: Keep the engraving density lighter around both eyes and inside the glasses. Preserve the person's present-day clothing and age. The final image must work as a modern academic avatar, not as a historical artifact.

Avoid: direct imitation of any award organization or branded artwork, award medals, laurels, currency engraving, banknote composition, generic historical dignitary, Victorian costume, excessive aging, sepia, ornate captions, seals, and emblems.
```

### 方案 8：深色学术雕刻

**定位：** 方案 7 的深色页面版本。它最容易与深色 Terminal 页面融为一体，但必须防止黑色背景吞没头发轮廓。

```text
Primary request: Transform the portrait into a modern scientific engraving on a deep neutral-charcoal background.

Scene/backdrop: Flat deep charcoal background with a clear tonal boundary around the hair and shoulders.

Style/medium: Fine white and light-gray ink engraving with controlled cross-hatching and stipple shading, like an original contemporary academic biography illustration. Crisp, high-contrast, elegant, and readable at small avatar size.

Lighting/mood: Thoughtful, scholarly, precise, calm, and approachable.

Additional constraints: Use only white and neutral-gray linework over charcoal. Separate dark hair from the background with controlled light-gray edge definition, not a glow. Keep the face dimensional without introducing a colored cast.

Avoid: direct branded imitation, cyberpunk styling, neon, glow, retro-game pixels, ornate vintage borders, excessive scratches, currency-like layout, halo effects, and lost hair edges.
```

## 6. 方案选择建议

| 优先级 | 方案 | 适合目标 | 主要风险 |
| --- | --- | --- | --- |
| 1 | 现代学术档案雕刻 | 学术辨识度与网站风格的最佳平衡 | 排线过密会影响小图阅读 |
| 2 | 深色学术雕刻 | 与默认深色页面自然融合 | 深色头发可能融入背景 |
| 3 | 技术杂志线描 | 现代、克制、技术导向 | 线条过少会弱化身份 |
| 4 | 纯灰阶编辑摄影 | 最大程度保留真实身份 | 个性弱于插画方案 |
| 5 | 木刻与版画 | 强烈、手工、视觉焦点明确 | 容易显得过旧或过重 |
| 6 | 极简钢笔 | 轻盈、亲和 | 容易卡通化或泛化 |
| 7 | 单色丝网印刷 | 图形感与记忆点强 | 大色块可能遮掉五官 |
| 8 | 终端抖动像素 | 最直接呼应 Terminal | 正式学术感相对较弱 |

建议先生成方案 7、方案 8 和方案 1 各一个版本，在网站真实的明暗主题中以 `220 x 220 px` 并排比较，再决定最终方向。

## 7. 迭代 Prompt 模板

每轮只修改一个问题，并重复身份约束。不要在同一轮同时要求改变构图、光影、纹理和表情。

### 提高身份相似度

```text
Keep the current visual style unchanged. Increase identity fidelity to Image 1 only: restore the exact face width, jaw shape, eye spacing, nose shape, mouth shape, glasses geometry, and hairstyle silhouette. Do not change pose, framing, background, or monochrome palette.
```

### 减少纹理干扰

```text
Keep identity, composition, and monochrome palette unchanged. Reduce hatching, stipple, or print texture by 30 percent around the eyes, lenses, nose, and mouth. Preserve texture elsewhere. Do not smooth or reshape the face.
```

### 增强小尺寸可读性

```text
Keep identity and style unchanged. Optimize only for readability at 220 x 220 pixels: clarify both eyes, glasses bridge, mouth line, jaw boundary, and hairstyle silhouette; simplify minor background and clothing detail. Do not exaggerate features.
```

### 清除残余色相

```text
Keep every shape, texture, value, and composition unchanged. Convert the entire image to strict achromatic grayscale with saturation exactly zero. Preserve tonal contrast. Do not add tinting, split toning, colored reflections, or chromatic edge artifacts.
```

## 8. 输出与验收

### 推荐输出

- 保存正方形 PNG 原图，建议至少 `1024 x 1024 px`；
- 另导出 `440 x 440 px` 和 `220 x 220 px` 预览，用于检查降采样效果；
- 不覆盖 `prev-information/personal/profile.png`，先使用版本化文件名保存候选结果；
- 候选命名示例：`avatar-engraving-v1.png`、`avatar-engraving-dark-v1.png`、`avatar-editorial-line-v1.png`。

### 验收清单

- [ ] 第一眼可以确认是本人，而非相似的通用人物；
- [ ] 镜框形状、鼻梁位置和镜腿连接自然；
- [ ] 发型外轮廓与输入照片一致；
- [ ] 双眼没有被纹理、反光或深阴影遮挡；
- [ ] 在 `220 x 220 px` 下五官仍清晰；
- [ ] 头顶、下巴和肩部裁切自然；
- [ ] 所有像素均为黑、白或中性灰，不存在残余色相；
- [ ] 没有文字、奖章、月桂、Logo、边框或水印；
- [ ] 明色和暗色网页背景上都不会丢失人物轮廓；
- [ ] 头像静态、克制，不包含交互终端或界面元素。

## 9. 最终建议

先以 `avatar-1.png` 为唯一身份参考生成方案 7。若人物辨识度通过，再基于同一结果制作方案 8，而不是重新生成一个身份不稳定的深色版本。方案 1 可作为更现代、更轻的对照组。其余方案适合探索，不应在首轮同时大量生成。
