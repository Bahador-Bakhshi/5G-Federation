graph [
  node [
    id 0
    label 1
    disk 8
    cpu 3
    memory 1
  ]
  node [
    id 1
    label 2
    disk 10
    cpu 1
    memory 1
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 2
    memory 7
  ]
  node [
    id 3
    label 4
    disk 3
    cpu 1
    memory 3
  ]
  node [
    id 4
    label 5
    disk 4
    cpu 4
    memory 2
  ]
  node [
    id 5
    label 6
    disk 1
    cpu 3
    memory 9
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 26
    bw 172
  ]
  edge [
    source 0
    target 1
    delay 26
    bw 175
  ]
  edge [
    source 0
    target 2
    delay 35
    bw 109
  ]
  edge [
    source 0
    target 3
    delay 30
    bw 194
  ]
  edge [
    source 1
    target 4
    delay 33
    bw 189
  ]
  edge [
    source 2
    target 5
    delay 31
    bw 166
  ]
  edge [
    source 3
    target 5
    delay 28
    bw 67
  ]
  edge [
    source 4
    target 5
    delay 28
    bw 119
  ]
]
