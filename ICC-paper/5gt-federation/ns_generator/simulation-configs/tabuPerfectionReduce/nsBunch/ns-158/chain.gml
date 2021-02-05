graph [
  node [
    id 0
    label 1
    disk 3
    cpu 2
    memory 1
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 3
    memory 7
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 2
    memory 2
  ]
  node [
    id 3
    label 4
    disk 5
    cpu 4
    memory 14
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 1
    memory 1
  ]
  node [
    id 5
    label 6
    disk 9
    cpu 2
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 112
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 92
  ]
  edge [
    source 1
    target 2
    delay 33
    bw 95
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 118
  ]
  edge [
    source 1
    target 4
    delay 27
    bw 148
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 88
  ]
  edge [
    source 3
    target 5
    delay 34
    bw 128
  ]
  edge [
    source 4
    target 5
    delay 32
    bw 117
  ]
]
