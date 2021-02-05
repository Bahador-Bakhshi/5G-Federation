graph [
  node [
    id 0
    label 1
    disk 5
    cpu 1
    memory 11
  ]
  node [
    id 1
    label 2
    disk 6
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 14
  ]
  node [
    id 3
    label 4
    disk 10
    cpu 3
    memory 6
  ]
  node [
    id 4
    label 5
    disk 8
    cpu 4
    memory 12
  ]
  node [
    id 5
    label 6
    disk 5
    cpu 1
    memory 13
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 30
    bw 131
  ]
  edge [
    source 0
    target 1
    delay 28
    bw 74
  ]
  edge [
    source 0
    target 2
    delay 30
    bw 154
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 128
  ]
  edge [
    source 1
    target 5
    delay 32
    bw 107
  ]
  edge [
    source 2
    target 5
    delay 33
    bw 173
  ]
  edge [
    source 3
    target 4
    delay 27
    bw 178
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 130
  ]
]
