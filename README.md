# test-stacked-prs
testing some stacked prs

<pre><code>
[---------------------------------------------------- aten::_softmax ---------------------------------------------------]
                                                                                                                  |  aten
30 threads: -------------------------------------------------------------------------------------------------------------
      self=[dtype=torch.bfloat16, is_contiguous=True, shape=torch.Size([60223])], dim=0, half_to_float=False      |  <span style="font-weight:bold;filter: contrast(70%) brightness(190%);color:green;">1.8 </span></span>
      self=[dtype=torch.bfloat16, is_contiguous=True, shape=torch.Size([2411, 378])], dim=0, half_to_float=False  |  <span style="font-weight:bold;filter: contrast(70%) brightness(190%);color:green;">6.1 </span></span>

Times are in milliseconds (ms).
</code></pre>
