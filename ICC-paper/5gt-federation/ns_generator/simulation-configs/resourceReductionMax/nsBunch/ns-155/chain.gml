graph [
  node [
    id 0
    label 1
    disk 6
    cpu 1
    memory 8
  ]
  node [
    id 1
    label 2
    disk 2
    cpu 3
    memory 8
  ]
  node [
    id 2
    label 3
    disk 8
    cpu 2
    memory 5
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 9
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 3
    memory 6
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 182
  ]
  edge [
    source 0
    target 1
    delay 25
    bw 92
  ]
  edge [
    source 1
    target 2
    delay 26
    bw 187
  ]
  edge [
    source 1
    target 3
    delay 25
    bw 63
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 56
  ]
  edge [
    source 2
    target 5
    delay 32
    bw 167
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 197
  ]
  edge [
    source 4
    target 5
    delay 31
    bw 93
  ]
]
