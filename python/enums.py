from enum import Enum, auto


class PipelineSteps(Enum):
    CHECKOUT = auto()
    BUILD = auto()
    TEST = auto()
    SAST = auto()
    STAGE_DEPLOY = auto()
    PROD_DEPLOY = auto()
    DAST = auto()


def main():
    print('\n'.join(str(x) for x in PipelineSteps))


if __name__ == '__main__':
    main()
