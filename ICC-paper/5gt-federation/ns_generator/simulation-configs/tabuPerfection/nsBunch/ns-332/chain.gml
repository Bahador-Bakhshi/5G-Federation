graph [
  node [
    id 0
    label 1
    disk 2
    cpu 1
    memory 13
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 4
    memory 9
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 3
    memory 2
  ]
  node [
    id 3
    label 4
    disk 8
    cpu 2
    memory 12
  ]
  node [
    id 4
    label 5
    disk 10
    cpu 1
    memory 10
  ]
  node [
    id 5
    label 6
    disk 2
    cpu 4
    memory 1
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 62
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 91
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 175
  ]
  edge [
    source 1
    target 3
    delay 32
    bw 128
  ]
  edge [
    source 2
    target 5
    delay 34
    bw 133
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 107
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 122
  ]
]
