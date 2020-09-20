graph [
  node [
    id 0
    label 1
    disk 5
    cpu 3
    memory 6
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 4
    memory 8
  ]
  node [
    id 2
    label 3
    disk 10
    cpu 1
    memory 6
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 4
    memory 3
  ]
  node [
    id 4
    label 5
    disk 9
    cpu 3
    memory 12
  ]
  node [
    id 5
    label 6
    disk 3
    cpu 2
    memory 15
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 134
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 84
  ]
  edge [
    source 1
    target 2
    delay 34
    bw 102
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 128
  ]
  edge [
    source 2
    target 5
    delay 28
    bw 185
  ]
  edge [
    source 3
    target 4
    delay 26
    bw 172
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 154
  ]
]
