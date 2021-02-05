graph [
  node [
    id 0
    label 1
    disk 6
    cpu 2
    memory 6
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 2
    memory 8
  ]
  node [
    id 2
    label 3
    disk 5
    cpu 4
    memory 12
  ]
  node [
    id 3
    label 4
    disk 1
    cpu 4
    memory 13
  ]
  node [
    id 4
    label 5
    disk 3
    cpu 4
    memory 10
  ]
  node [
    id 5
    label 6
    disk 7
    cpu 4
    memory 11
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 146
  ]
  edge [
    source 0
    target 1
    delay 31
    bw 101
  ]
  edge [
    source 1
    target 2
    delay 31
    bw 130
  ]
  edge [
    source 1
    target 3
    delay 34
    bw 96
  ]
  edge [
    source 1
    target 4
    delay 28
    bw 79
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 142
  ]
  edge [
    source 3
    target 5
    delay 29
    bw 133
  ]
  edge [
    source 4
    target 5
    delay 29
    bw 182
  ]
]
