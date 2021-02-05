graph [
  node [
    id 0
    label 1
    disk 1
    cpu 4
    memory 4
  ]
  node [
    id 1
    label 2
    disk 7
    cpu 3
    memory 3
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 2
    memory 15
  ]
  node [
    id 3
    label 4
    disk 2
    cpu 1
    memory 11
  ]
  node [
    id 4
    label 5
    disk 2
    cpu 2
    memory 2
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 3
    memory 8
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 116
  ]
  edge [
    source 0
    target 1
    delay 34
    bw 50
  ]
  edge [
    source 0
    target 2
    delay 31
    bw 154
  ]
  edge [
    source 1
    target 3
    delay 33
    bw 118
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 163
  ]
  edge [
    source 3
    target 4
    delay 32
    bw 188
  ]
  edge [
    source 4
    target 5
    delay 34
    bw 123
  ]
]
