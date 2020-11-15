from graphlib import TopologicalSorter
from enums import PipelineSteps


def main():
    pipeline = {
        PipelineSteps.BUILD: {PipelineSteps.CHECKOUT},
        PipelineSteps.SAST: {PipelineSteps.BUILD},
        PipelineSteps.DAST: {PipelineSteps.STAGE_DEPLOY},
        PipelineSteps.STAGE_DEPLOY: {PipelineSteps.TEST},
        PipelineSteps.PROD_DEPLOY: {
            PipelineSteps.SAST,
            PipelineSteps.DAST,
        },
        PipelineSteps.TEST: {PipelineSteps.BUILD},
        PipelineSteps.CHECKOUT: {},
    }

    sorter = TopologicalSorter(pipeline)
    print('\n'.join(str(x) for x in sorter.static_order()))


if __name__ == '__main__':
    main()
