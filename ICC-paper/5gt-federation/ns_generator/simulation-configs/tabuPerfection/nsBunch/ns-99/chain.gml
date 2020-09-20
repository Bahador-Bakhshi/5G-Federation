graph [
  node [
    id 0
    label 1
    disk 7
    cpu 4
    memory 2
  ]
  node [
    id 1
    label 2
    disk 5
    cpu 1
    memory 4
  ]
  node [
    id 2
    label 3
    disk 6
    cpu 1
    memory 15
  ]
  node [
    id 3
    label 4
    disk 4
    cpu 4
    memory 4
  ]
  node [
    id 4
    label 5
    disk 7
    cpu 4
    memory 15
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 2
    memory 14
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 34
    bw 66
  ]
  edge [
    source 0
    target 1
    delay 32
    bw 182
  ]
  edge [
    source 0
    target 2
    delay 32
    bw 133
  ]
  edge [
    source 0
    target 3
    delay 31
    bw 146
  ]
  edge [
    source 1
    target 4
    delay 34
    bw 125
  ]
  edge [
    source 2
    target 4
    delay 28
    bw 153
  ]
  edge [
    source 3
    target 4
    delay 30
    bw 155
  ]
  edge [
    source 4
    target 5
    delay 35
    bw 149
  ]
]
