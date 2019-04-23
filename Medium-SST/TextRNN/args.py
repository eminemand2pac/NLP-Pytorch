import argparse


def get_args():
    data_dir = "data/SST2"
    cache_dir = data_dir +"/cache/"
    embedding_folder = "/home/songyingxin/datasets/WordEmbedding/"

    parser = argparse.ArgumentParser(description='SST')

    parser.add_argument("--seed", default=1234, type=int, help="随机种子")

    # data_util
    parser.add_argument(
        "--data_path", default=data_dir, type=str, help="sst2 数据集位置")
    parser.add_argument(
        "--cache_path", default=cache_dir, type=str, help="数据缓存地址"
    )
    parser.add_argument(
        "--sequence_length", default=60, type=int, help="句子长度"
    )

    # 优化参数
    parser.add_argument("--batch_size", default=64, type=int)
    parser.add_argument("--epoch_num", default=5, type=int)
    parser.add_argument("--dropout", default=0.4, type=float)

    # 模型参数
    parser.add_argument("--output_dim", default=1, type=int)

    # TextRNN 参数
    parser.add_argument("--hidden_size", default=60, type=int, help="隐层单元数")
    parser.add_argument('--num_layers', default=2, type=int, help='RNN层数')
    parser.add_argument("--bidirectional", default=True, type=bool)


    # word Embedding
    parser.add_argument(
        '--glove_word_file',
        default=embedding_folder + 'glove/glove.840B.300d.txt',
        type=str, help='path of word embedding file')
    parser.add_argument(
        '--glove_word_size',
        default=int(2.2e6), type=int,
        help='Corpus size for Glove')
    parser.add_argument(
        '--glove_word_dim',
        default=300, type=int,
        help='word embedding size (default: 300)')

    # char embedding
    parser.add_argument(
        '--glove_char_file',
        default=embedding_folder + "glove/glove.840B.300d-char.txt",
        type=str, help='path of char embedding file')
    parser.add_argument(
        '--glove_char_size',
        default=94, type=int,
        help='Corpus size for char embedding')
    parser.add_argument(
        '--glove_char_dim',
        default=300, type=int,
        help='char embedding size (default: 64)')
    

    config = parser.parse_args()

    return config