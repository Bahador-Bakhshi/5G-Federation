graph [
  node [
    id 0
    label 1
    disk 5
    cpu 4
    memory 8
  ]
  node [
    id 1
    label 2
    disk 3
    cpu 1
    memory 3
  ]
  node [
    id 2
    label 3
    disk 9
    cpu 3
    memory 4
  ]
  node [
    id 3
    label 4
    disk 9
    cpu 2
    memory 4
  ]
  node [
    id 4
    label 5
    disk 1
    cpu 1
    memory 10
  ]
  node [
    id 5
    label 6
    disk 6
    cpu 4
    memory 4
  ]
  node [
    id 6
    label "start"
  ]
  edge [
    source 0
    target 6
    delay 31
    bw 177
  ]
  edge [
    source 0
    target 1
    delay 30
    bw 143
  ]
  edge [
    source 0
    target 2
    delay 26
    bw 189
  ]
  edge [
    source 1
    target 3
    delay 26
    bw 116
  ]
  edge [
    source 2
    target 3
    delay 35
    bw 171
  ]
  edge [
    source 3
    target 4
    delay 25
    bw 172
  ]
  edge [
    source 4
    target 5
    delay 27
    bw 121
  ]
]
